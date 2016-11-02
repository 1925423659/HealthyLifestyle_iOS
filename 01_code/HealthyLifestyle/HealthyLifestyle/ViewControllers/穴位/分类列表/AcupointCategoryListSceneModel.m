//
//  MessageSceneModel.m
//  ZhaoQiPei
//
//  Created by 找汽配 on 16/3/17.
//  Copyright © 2016年 祥运. All rights reserved.
//

#import "AcupointCategoryListSceneModel.h"

@implementation AcupointCategoryListSceneModel

- (void)loadSceneModel {
    [super loadSceneModel];

    self.categoryList = @[[ControllerModel modelWithDict:@{@"title":NSLocalizedString(@"按经脉浏览", nil),
                                                           @"controller":@"MeridianListScene"}],
                          [ControllerModel modelWithDict:@{@"title":NSLocalizedString(@"按位置浏览", nil),
                                                           @"controller":@""}],
                          [ControllerModel modelWithDict:@{@"title":NSLocalizedString(@"按主治症状浏览", nil),
                                                           @"controller":@"FunctionListScene"}],
                          [ControllerModel modelWithDict:@{@"title":NSLocalizedString(@"搜索", nil),
                                                           @"controller":@""}]];
}

@end
